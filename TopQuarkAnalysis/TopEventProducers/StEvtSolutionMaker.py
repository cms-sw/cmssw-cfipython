import FWCore.ParameterSet.Config as cms

def StEvtSolutionMaker(*args, **kwargs):
  mod = cms.EDProducer('StEvtSolutionMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
