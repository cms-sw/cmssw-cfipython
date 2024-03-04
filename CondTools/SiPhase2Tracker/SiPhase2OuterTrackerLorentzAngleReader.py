import FWCore.ParameterSet.Config as cms

def SiPhase2OuterTrackerLorentzAngleReader(**kwargs):
  mod = cms.EDAnalyzer('SiPhase2OuterTrackerLorentzAngleReader',
    printDebug = cms.untracked.uint32(5),
    label = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
