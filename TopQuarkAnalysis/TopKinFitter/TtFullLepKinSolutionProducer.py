import FWCore.ParameterSet.Config as cms

def TtFullLepKinSolutionProducer(**kwargs):
  mod = cms.EDProducer('TtFullLepKinSolutionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
