import FWCore.ParameterSet.Config as cms

def EcalDeadCellDeltaRFilter(**kwargs):
  mod = cms.EDFilter('EcalDeadCellDeltaRFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
