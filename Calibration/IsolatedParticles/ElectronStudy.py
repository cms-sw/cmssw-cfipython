import FWCore.ParameterSet.Config as cms

def ElectronStudy(**kwargs):
  mod = cms.EDAnalyzer('ElectronStudy',
    ModuleLabel = cms.untracked.string('g4SimHits'),
    EBCollection = cms.untracked.string('EcalHitsEB'),
    EECollection = cms.untracked.string('EcalHitsEE'),
    Verbosity = cms.untracked.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
