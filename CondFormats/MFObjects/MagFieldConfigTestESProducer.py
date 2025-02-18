import FWCore.ParameterSet.Config as cms

def MagFieldConfigTestESProducer(*args, **kwargs):
  mod = cms.ESProducer('MagFieldConfigTestESProducer',
    configs = cms.VPSet(
      template = cms.PSetTemplate(
        run = cms.required.uint32,
        config = cms.PSet()
      )
    ),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
