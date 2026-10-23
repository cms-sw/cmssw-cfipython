import FWCore.ParameterSet.Config as cms

def TtFullLepKinSolutionProducer(*args, **kwargs):
  mod = cms.EDProducer('TtFullLepKinSolutionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
