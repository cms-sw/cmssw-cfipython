import FWCore.ParameterSet.Config as cms

def HcalTimeSlewEP(*args, **kwargs):
  mod = cms.ESSource('HcalTimeSlewEP',
    timeSlewParametersM2 = cms.VPSet(
      cms.PSet(),
      template = cms.PSetTemplate(
        tzero = cms.required.double,
        slope = cms.required.double,
        tmax = cms.required.double
      )
    ),
    timeSlewParametersM3 = cms.VPSet(
      cms.PSet(),
      template = cms.PSetTemplate(
        cap = cms.required.double,
        tspar0 = cms.required.double,
        tspar1 = cms.required.double,
        tspar2 = cms.required.double,
        tspar0_siPM = cms.required.double,
        tspar1_siPM = cms.required.double,
        tspar2_siPM = cms.required.double
      )
    ),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
