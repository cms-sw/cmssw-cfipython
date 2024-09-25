import FWCore.ParameterSet.Config as cms

def HepPDTESSource(*args, **kwargs):
  mod = cms.ESSource('HepPDTESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
