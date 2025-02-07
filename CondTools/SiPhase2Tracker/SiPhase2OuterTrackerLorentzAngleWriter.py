import FWCore.ParameterSet.Config as cms

def SiPhase2OuterTrackerLorentzAngleWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPhase2OuterTrackerLorentzAngleWriter',
    record = cms.string('SiPhase2OuterTrackerLorentzAngleRcd'),
    tag = cms.string('SiPhase2OuterTrackerLorentzAngle'),
    value = cms.double(0.07),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
