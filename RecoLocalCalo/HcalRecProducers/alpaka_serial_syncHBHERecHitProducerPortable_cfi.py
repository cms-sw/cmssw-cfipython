import FWCore.ParameterSet.Config as cms

alpaka_serial_syncHBHERecHitProducerPortable = cms.EDProducer('alpaka_serial_sync::HBHERecHitProducerPortable',
  mahiPulseOffSets = cms.ESInputTag('', ''),
  maxTimeSamples = cms.uint32(10),
  kprep1dChannelsPerBlock = cms.uint32(32),
  digisLabelF01HE = cms.InputTag('hcalRawToDigiGPU', 'f01HEDigisGPU'),
  digisLabelF5HB = cms.InputTag('hcalRawToDigiGPU', 'f5HBDigisGPU'),
  digisLabelF3HB = cms.InputTag('hcalRawToDigiGPU', 'f3HBDigisGPU'),
  recHitsLabelM0HBHE = cms.string('recHitsM0HBHE'),
  sipmQTSShift = cms.int32(0),
  sipmQNTStoSum = cms.int32(3),
  firstSampleShift = cms.int32(0),
  useEffectivePedestals = cms.bool(True),
  meanTime = cms.double(0),
  timeSigmaSiPM = cms.double(2.5),
  timeSigmaHPD = cms.double(5),
  ts4Thresh = cms.double(0),
  applyTimeSlew = cms.bool(True),
  tzeroTimeSlewParameters = cms.vdouble(
    23.960177,
    11.977461,
    9.109694
  ),
  slopeTimeSlewParameters = cms.vdouble(
    -3.178648,
    -1.5610227,
    -1.075824
  ),
  tmaxTimeSlewParameters = cms.vdouble(
    16,
    10,
    6.25
  ),
  kernelMinimizeThreads = cms.vuint32(
    16,
    1,
    1
  ),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
