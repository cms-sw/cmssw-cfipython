import FWCore.ParameterSet.Config as cms

def SiStripApvGainInspector(**kwargs):
  mod = cms.EDAnalyzer('SiStripApvGainInspector',
    inputFile = cms.untracked.string(''),
    minNrEntries = cms.untracked.double(20),
    fitMode = cms.int32(2),
    selectedModules = cms.untracked.vuint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
