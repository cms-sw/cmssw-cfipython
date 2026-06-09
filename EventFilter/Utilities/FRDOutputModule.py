import FWCore.ParameterSet.Config as cms

def FRDOutputModule(*args, **kwargs):
  mod = cms.OutputModule('FRDOutputModule',
    source = cms.InputTag('rawDataCollector'),
    frdFileVersion = cms.untracked.uint32(1),
    frdVersion = cms.untracked.uint32(6),
    filePrefix = cms.untracked.string(''),
    fileName = cms.untracked.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
