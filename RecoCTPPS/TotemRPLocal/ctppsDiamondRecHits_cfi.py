import FWCore.ParameterSet.Config as cms

ctppsDiamondRecHits = cms.EDProducer('CTPPSDiamondRecHitProducer',
  digiTag = cms.InputTag('ctppsDiamondRawToDigi', 'TimingDiamond'),
  timeSliceNs = cms.double(0.0244140625),
  timeShift = cms.int32(0)
)
