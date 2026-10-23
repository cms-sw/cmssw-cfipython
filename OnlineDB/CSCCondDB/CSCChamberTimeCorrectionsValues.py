import FWCore.ParameterSet.Config as cms

def CSCChamberTimeCorrectionsValues(*args, **kwargs):
  mod = cms.ESSource('CSCChamberTimeCorrectionsValues',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
