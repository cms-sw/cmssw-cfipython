import FWCore.ParameterSet.Config as cms

def SiPhase2OuterTrackerLorentzAngleWriter(**kwargs):
  mod = cms.EDAnalyzer('SiPhase2OuterTrackerLorentzAngleWriter',
    record = cms.string('SiPhase2OuterTrackerLorentzAngleRcd'),
    tag = cms.string('SiPhase2OuterTrackerLorentzAngle'),
    value = cms.double(0.07),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
