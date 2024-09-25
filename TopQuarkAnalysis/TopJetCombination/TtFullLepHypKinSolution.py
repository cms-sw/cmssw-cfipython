import FWCore.ParameterSet.Config as cms

def TtFullLepHypKinSolution(*args, **kwargs):
  mod = cms.EDProducer('TtFullLepHypKinSolution',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
