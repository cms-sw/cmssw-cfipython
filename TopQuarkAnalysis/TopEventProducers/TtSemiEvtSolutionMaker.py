import FWCore.ParameterSet.Config as cms

def TtSemiEvtSolutionMaker(**kwargs):
  mod = cms.EDProducer('TtSemiEvtSolutionMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
