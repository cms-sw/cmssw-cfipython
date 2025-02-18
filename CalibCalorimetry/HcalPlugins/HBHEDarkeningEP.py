import FWCore.ParameterSet.Config as cms

def HBHEDarkeningEP(*args, **kwargs):
  mod = cms.ESSource('HBHEDarkeningEP',
    ieta_shift = cms.required.int32,
    drdA = cms.required.double,
    drdB = cms.required.double,
    dosemaps = cms.VPSet(
      cms.PSet(),
      template = cms.PSetTemplate(
        energy = cms.required.int32,
        file = cms.required.FileInPath
      )
    ),
    years = cms.VPSet(
      cms.PSet(),
      template = cms.PSetTemplate(
        year = cms.required.string,
        intlumi = cms.required.double,
        lumirate = cms.required.double,
        energy = cms.required.int32
      )
    ),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
