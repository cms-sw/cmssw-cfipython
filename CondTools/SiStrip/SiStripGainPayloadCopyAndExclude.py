import FWCore.ParameterSet.Config as cms

def SiStripGainPayloadCopyAndExclude(**kwargs):
  mod = cms.EDAnalyzer('SiStripGainPayloadCopyAndExclude',
    excludedModules = cms.untracked.vuint32(),
    record = cms.untracked.string('SiStripApvGainRcd'),
    gainType = cms.untracked.uint32(1),
    reverseSelection = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
