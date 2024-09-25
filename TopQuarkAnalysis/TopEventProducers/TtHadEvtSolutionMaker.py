import FWCore.ParameterSet.Config as cms

def TtHadEvtSolutionMaker(*args, **kwargs):
  mod = cms.EDProducer('TtHadEvtSolutionMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
