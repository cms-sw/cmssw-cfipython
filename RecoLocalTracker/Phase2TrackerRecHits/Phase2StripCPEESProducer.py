import FWCore.ParameterSet.Config as cms

def Phase2StripCPEESProducer(*args, **kwargs):
  mod = cms.ESProducer('Phase2StripCPEESProducer',
    ComponentType = cms.string('Phase2StripCPE'),
    parameters = cms.PSet(
      TanLorentzAnglePerTesla = cms.double(0.07),
      LorentzAngle_DB = cms.bool(True)
    ),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
