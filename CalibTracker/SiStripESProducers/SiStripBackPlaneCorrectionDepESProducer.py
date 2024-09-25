import FWCore.ParameterSet.Config as cms

def SiStripBackPlaneCorrectionDepESProducer(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
