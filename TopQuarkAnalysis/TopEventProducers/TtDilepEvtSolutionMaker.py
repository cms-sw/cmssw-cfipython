import FWCore.ParameterSet.Config as cms

def TtDilepEvtSolutionMaker(**kwargs):
  mod = cms.EDProducer('TtDilepEvtSolutionMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
