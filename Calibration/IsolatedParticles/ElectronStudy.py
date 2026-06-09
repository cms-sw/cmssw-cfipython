import FWCore.ParameterSet.Config as cms

def ElectronStudy(*args, **kwargs):
  mod = cms.EDAnalyzer('ElectronStudy',
    ModuleLabel = cms.untracked.string('g4SimHits'),
    EBCollection = cms.untracked.string('EcalHitsEB'),
    EECollection = cms.untracked.string('EcalHitsEE'),
    Verbosity = cms.untracked.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
