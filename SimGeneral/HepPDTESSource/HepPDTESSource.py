import FWCore.ParameterSet.Config as cms

def HepPDTESSource(**kwargs):
  mod = cms.ESSource('HepPDTESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
