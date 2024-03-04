import FWCore.ParameterSet.Config as cms

def EcalDeadCellBoundaryEnergyFilter(**kwargs):
  mod = cms.EDFilter('EcalDeadCellBoundaryEnergyFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
