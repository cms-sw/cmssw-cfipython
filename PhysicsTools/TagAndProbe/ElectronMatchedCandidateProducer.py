import FWCore.ParameterSet.Config as cms

def ElectronMatchedCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('ElectronMatchedCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
