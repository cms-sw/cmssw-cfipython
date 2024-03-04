import FWCore.ParameterSet.Config as cms

def TtHadEvtSolutionMaker(**kwargs):
  mod = cms.EDProducer('TtHadEvtSolutionMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
