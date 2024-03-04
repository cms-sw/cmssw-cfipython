import FWCore.ParameterSet.Config as cms

def TtFullLepHypKinSolution(**kwargs):
  mod = cms.EDProducer('TtFullLepHypKinSolution',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
