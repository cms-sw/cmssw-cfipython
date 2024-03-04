import FWCore.ParameterSet.Config as cms

def HLTSiPhase2TrackerClusterMultiplicityValueProducer(**kwargs):
  mod = cms.EDProducer('HLTSiPhase2TrackerClusterMultiplicityValueProducer',
    src = cms.InputTag(''),
    defaultValue = cms.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
