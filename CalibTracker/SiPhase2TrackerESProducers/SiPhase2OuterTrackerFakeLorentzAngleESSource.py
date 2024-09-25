import FWCore.ParameterSet.Config as cms

def SiPhase2OuterTrackerFakeLorentzAngleESSource(*args, **kwargs):
  mod = cms.ESSource('SiPhase2OuterTrackerFakeLorentzAngleESSource',
    LAValue = cms.double(0.07),
    recordName = cms.string('LorentzAngle'),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
