import FWCore.ParameterSet.Config as cms

hcalIsoTrackAnalyzer = cms.EDAnalyzer('HcalIsoTrackAnalyzer',
  momentumLow = cms.double(40),
  momentumHigh = cms.double(60),
  useRaw = cms.untracked.int32(0),
  dataType = cms.untracked.int32(0),
  isoTrackVarLabel = cms.InputTag('alcaHcalIsotrkProducer', 'HcalIsoTrack'),
  isoTrackEvtLabel = cms.InputTag('alcaHcalIsotrkProducer', 'HcalIsoTrackEvent'),
  mightGet = cms.optional.untracked.vstring
)
