import FWCore.ParameterSet.Config as cms

def CSCChamberTimeCorrectionsValues(**kwargs):
  mod = cms.ESSource('CSCChamberTimeCorrectionsValues',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
