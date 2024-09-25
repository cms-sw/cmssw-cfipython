import FWCore.ParameterSet.Config as cms

def HLTSiPhase2TrackerClusterMultiplicityValueProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTSiPhase2TrackerClusterMultiplicityValueProducer',
    src = cms.InputTag(''),
    defaultValue = cms.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
