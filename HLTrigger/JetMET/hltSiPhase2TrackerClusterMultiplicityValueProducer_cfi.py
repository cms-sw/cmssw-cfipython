import FWCore.ParameterSet.Config as cms

hltSiPhase2TrackerClusterMultiplicityValueProducer = cms.EDProducer('HLTSiPhase2TrackerClusterMultiplicityValueProducer',
  src = cms.InputTag(''),
  defaultValue = cms.double(0),
  mightGet = cms.optional.untracked.vstring
)
