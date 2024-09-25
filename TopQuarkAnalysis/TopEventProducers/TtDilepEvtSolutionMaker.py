import FWCore.ParameterSet.Config as cms

def TtDilepEvtSolutionMaker(*args, **kwargs):
  mod = cms.EDProducer('TtDilepEvtSolutionMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
