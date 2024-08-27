import FWCore.ParameterSet.Config as cms

def SiStripLorentzAngleDepESProducer(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
