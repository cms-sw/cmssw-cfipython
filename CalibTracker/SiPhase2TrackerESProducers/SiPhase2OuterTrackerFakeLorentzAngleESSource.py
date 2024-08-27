import FWCore.ParameterSet.Config as cms

def SiPhase2OuterTrackerFakeLorentzAngleESSource(**kwargs):
  mod = cms.ESSource('SiPhase2OuterTrackerFakeLorentzAngleESSource',
    LAValue = cms.double(0.07),
    recordName = cms.string('LorentzAngle'),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
