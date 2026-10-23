import FWCore.ParameterSet.Config as cms

def SiStripGainPayloadCopyAndExclude(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripGainPayloadCopyAndExclude',
    excludedModules = cms.untracked.vuint32(),
    record = cms.untracked.string('SiStripApvGainRcd'),
    gainType = cms.untracked.uint32(1),
    reverseSelection = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
