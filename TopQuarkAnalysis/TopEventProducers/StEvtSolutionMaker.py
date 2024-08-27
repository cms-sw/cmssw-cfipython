import FWCore.ParameterSet.Config as cms

def StEvtSolutionMaker(**kwargs):
  mod = cms.EDProducer('StEvtSolutionMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
