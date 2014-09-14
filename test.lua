scriptId = 'com.nihar.testing'

scriptName = "test.lua"
openCloseSequence = {'s','u','d','o','space','p','y','t','h','o','n','space','m','o','t','o','r','period','p','y','return'}
lightSequence = { 's', 'u', 'd', 'o', 'space', 'p','y','t','h','o','n', 'space', 'b', 'u', 'l', 'b', 'period', 'p', 'y', 'return'}
seatUpSequence = { 's', 'u', 'd', 'o', 'space', 'p', 'y', 't', 'h', 'o', 'n', 'space', 's', 'e', 'a', 't', 'u', 'p', 'period', 'p', 'y', 'return'}
seatDownSequence = { 's', 'u', 'd', 'o', 'space', 'p', 'y', 't', 'h', 'o', 'n', 'space', 's', 'e', 'a', 't', 'd', 'o', 'w', 'n', 'period', 'p', 'y', 'return'}
ledOnSequence = { 's', 'u', 'd', 'o', 'space', 'p', 'y', 't', 'h', 'o', 'n', 'space', 'l', 'e', 'd', 'o', 'n', 'period', 'p', 'y', 'return'}
ledOffSequence = { 's', 'u', 'd', 'o', 'space', 'p', 'y', 't', 'h', 'o', 'n', 'space', 'l', 'e', 'd', 'o', 'f', 'f', 'period', 'p', 'y', 'return'}
fanOnSequence = { 's', 'u', 'd', 'o', 'space', 'p', 'y', 't', 'h', 'o', 'n', 'space', 'f', 'a', 'n', 'o', 'n', 'period', 'p', 'y', 'return'}
fanOffSequence = { 's', 'u', 'd', 'o', 'space', 'p', 'y', 't', 'h', 'o', 'n', 'space', 'f', 'a', 'n', 'o', 'f', 'f', 'period', 'p', 'y', 'return'}
InUseSequence = { 's', 'u', 'd', 'o', 'space', 'p', 'y', 't', 'h', 'o', 'n', 'space', 'l', 'c', 'd', 'period', 'p', 'y', 'return'}
NotInUseSequence = { 's', 'u', 'd', 'o', 'space', 'p', 'y', 't', 'h', 'o', 'n', 'space', 'l', 'c', 'd', '2', 'period', 'p', 'y', 'return'}



--SeatUp and SeatDown are WaveIn
--LedOn and LedOff are fingersSpread or Fist


time = myo.getTimeMilliseconds()
curTime = 0
isSeatUp = false
isLightOn = false
isFanOn = false

function activeAppName()
	myo.debug("This script is " .. scriptName);
	return scriptName
end

function onForegroundWindowChange(app, title)
	myo.debug("onForegroundWindowChange: " .. app .. ", " .. title)
	return true
end

function onActiveChange(isActive)
	myo.debug("onActiveChange")
end

function GestureResponse(keystrokes)
	length = #keystrokes
	myo.debug("Length of received array: " .. length)
	for i=1,length do
		myo.keyboard(keystrokes[i], "press")
	end
end
	
function onPoseEdge(pose, edge)
	myo.debug("onPoseEdge: " .. pose .. ", " .. edge)
	myo.debug(myo.getPitch())
	if myo.getPitch() >= .5 or myo.getPitch() <= -.5 then
		if pose=="waveIn" or pose == "waveOut" then
			mytime = time
			if curTime - mytime > 3000 then
				time = curTime
				if isSeatUp then
					isSeatUp = false
					GestureResponse(seatDownSequence)
				elseif isSeatUp == false then
					isSeatUp = true
					GestureResponse(seatUpSequence)
				end
			end

		end
		if pose=="fingersSpread" or pose=="fist" then
			mytime = time
			if curTime - mytime > 3000 then
				time = curTime
				if isLightOn then
					isLightOn = false
					GestureResponse(ledOffSequence)
					GestureResponse(NotInUseSequence)

				elseif isLightOn == false then
					isLightOn = true
					GestureResponse(ledOnSequence)
					GestureResponse(InUseSequence)
				end
			end
		end
	end
	if math.abs(myo.getPitch()) <= .5 and math.abs(myo.getYaw()) >= .6 then
		if pose == "waveIn" or pose == "waveOut" then
			mytime = time
			if curTime - mytime > 3000 then
				time = curTime
				if isFanOn then
					isFanOn = false
					GestureResponse(fanOffSequence)
				elseif isFanOn == false then
					isFanOn = true
					GestureResponse(fanOnSequence)
				end
			end
		end
	end
end
	

function onPeriodic()
	curTime = myo.getTimeMilliseconds()
end
