import FWCore.ParameterSet.Config as cms

def TtSemiEvtSolutionMaker(*args, **kwargs):
  mod = cms.EDProducer('TtSemiEvtSolutionMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
