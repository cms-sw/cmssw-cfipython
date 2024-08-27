import FWCore.ParameterSet.Config as cms

def FRDOutputModule(**kwargs):
  mod = cms.OutputModule('FRDOutputModule',
    source = cms.InputTag('rawDataCollector'),
    frdFileVersion = cms.untracked.uint32(1),
    frdVersion = cms.untracked.uint32(6),
    filePrefix = cms.untracked.string(''),
    fileName = cms.untracked.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
