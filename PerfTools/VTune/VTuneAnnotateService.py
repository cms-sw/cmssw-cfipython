import FWCore.ParameterSet.Config as cms

def VTuneAnnotateService(*args, **kwargs):
  mod = cms.Service('VTuneAnnotateService',
    moduleNames = cms.untracked.vstring(),
    allModules = cms.untracked.bool(False),
    ittDomain = cms.untracked.string('CMSSW.ModuleTracker')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
