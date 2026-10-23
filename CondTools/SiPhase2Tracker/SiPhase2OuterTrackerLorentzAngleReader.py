import FWCore.ParameterSet.Config as cms

def SiPhase2OuterTrackerLorentzAngleReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPhase2OuterTrackerLorentzAngleReader',
    printDebug = cms.untracked.uint32(5),
    label = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
