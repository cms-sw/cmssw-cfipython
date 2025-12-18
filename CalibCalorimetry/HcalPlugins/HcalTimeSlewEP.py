import FWCore.ParameterSet.Config as cms

def HcalTimeSlewEP(*args, **kwargs):
  mod = cms.ESSource('HcalTimeSlewEP',
    appendToDataLabel = cms.string('HBHE'),
    timeSlewParametersM2 = cms.VPSet(
      cms.PSet(
        slope = cms.double(-3.178648),
        tmax = cms.double(16),
        tzero = cms.double(23.960177)
      ),
      cms.PSet(
        slope = cms.double(-1.5610227),
        tmax = cms.double(10),
        tzero = cms.double(11.977461)
      ),
      cms.PSet(
        slope = cms.double(-1.075824),
        tmax = cms.double(6.25),
        tzero = cms.double(9.109694)
      ),
      template = cms.PSetTemplate(
        tzero = cms.double(23.960177),
        slope = cms.double(-3.178648),
        tmax = cms.double(16)
      )
    ),
    timeSlewParametersM3 = cms.VPSet(
      cms.PSet(
        cap = cms.double(6),
        tspar0 = cms.double(12.2999),
        tspar0_siPM = cms.double(0),
        tspar1 = cms.double(-2.19142),
        tspar1_siPM = cms.double(0),
        tspar2 = cms.double(0),
        tspar2_siPM = cms.double(0)
      ),
      cms.PSet(
        cap = cms.double(6),
        tspar0 = cms.double(15.5),
        tspar0_siPM = cms.double(0),
        tspar1 = cms.double(-3.2),
        tspar1_siPM = cms.double(0),
        tspar2 = cms.double(32),
        tspar2_siPM = cms.double(0)
      ),
      cms.PSet(
        cap = cms.double(6),
        tspar0 = cms.double(12.2999),
        tspar0_siPM = cms.double(0),
        tspar1 = cms.double(-2.19142),
        tspar1_siPM = cms.double(0),
        tspar2 = cms.double(0),
        tspar2_siPM = cms.double(0)
      ),
      cms.PSet(
        cap = cms.double(6),
        tspar0 = cms.double(12.2999),
        tspar0_siPM = cms.double(0),
        tspar1 = cms.double(-2.19142),
        tspar1_siPM = cms.double(0),
        tspar2 = cms.double(0),
        tspar2_siPM = cms.double(0)
      ),
      template = cms.PSetTemplate(
        cap = cms.double(6),
        tspar0 = cms.double(12.2999),
        tspar1 = cms.double(-2.19142),
        tspar2 = cms.double(0),
        tspar0_siPM = cms.double(0),
        tspar1_siPM = cms.double(0),
        tspar2_siPM = cms.double(0)
      )
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
