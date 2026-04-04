import FWCore.ParameterSet.Config as cms

def SiStripLorentzAngleDepESProducer(*args, **kwargs):
  mod = cms.ESProducer('SiStripLorentzAngleDepESProducer',
    LatencyRecord = cms.PSet(
      record = cms.string('SiStripLatencyRcd'),
      label = cms.untracked.string('')
    ),
    LorentzAnglePeakMode = cms.PSet(
      record = cms.string('SiStripLorentzAngleRcd'),
      label = cms.untracked.string('peak')
    ),
    LorentzAngleDeconvMode = cms.PSet(
      record = cms.string('SiStripLorentzAngleRcd'),
      label = cms.untracked.string('deconvolution')
    ),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
