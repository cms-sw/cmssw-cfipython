import FWCore.ParameterSet.Config as cms

def SiStripApvGainInspector(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripApvGainInspector',
    inputFile = cms.untracked.string(''),
    minNrEntries = cms.untracked.double(20),
    fitMode = cms.int32(2),
    selectedModules = cms.untracked.vuint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
