import FWCore.ParameterSet.Config as cms

alcaHcalIsotrkFilter = cms.EDFilter('AlCaHcalIsotrkFilter',
  momentumLow = cms.double(40),
  momentumHigh = cms.double(60),
  prescaleLow = cms.int32(1),
  prescaleHigh = cms.int32(1),
  isoTrackLabel = cms.InputTag('alcaHcalIsotrkProducer', 'HcalIsoTrack'),
  mightGet = cms.optional.untracked.vstring
)
