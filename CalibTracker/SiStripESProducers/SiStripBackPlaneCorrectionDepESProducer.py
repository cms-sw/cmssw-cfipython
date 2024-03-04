import FWCore.ParameterSet.Config as cms

def SiStripBackPlaneCorrectionDepESProducer(**kwargs):
  mod = cms.ESProducer('SiStripBackPlaneCorrectionDepESProducer',
    LatencyRecord = cms.PSet(
      record = cms.string('SiStripLatencyRcd'),
      label = cms.untracked.string('')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
      record = cms.string('SiStripBackPlaneCorrectionRcd'),
      label = cms.untracked.string('peak')
    ),
    BackPlaneCorrectionDeconvMode = cms.PSet(
      record = cms.string('SiStripBackPlaneCorrectionRcd'),
      label = cms.untracked.string('deconvolution')
    ),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
