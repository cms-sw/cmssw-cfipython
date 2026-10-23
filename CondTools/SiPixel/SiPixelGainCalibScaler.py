import FWCore.ParameterSet.Config as cms

def SiPixelGainCalibScaler(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelGainCalibScaler',
    record = cms.string('SiPixelGainCalibrationForHLTRcd'),
    isForHLT = cms.bool(True),
    parameters = cms.VPSet(
      cms.PSet(
        conversionFactor = cms.double(65),
        conversionFactorL1 = cms.double(65),
        offset = cms.double(-414),
        offsetL1 = cms.double(-414),
        phase = cms.uint32(0)
      ),
      cms.PSet(
        conversionFactor = cms.double(47),
        conversionFactorL1 = cms.double(50),
        offset = cms.double(-60),
        offsetL1 = cms.double(-670),
        phase = cms.uint32(1)
      ),
      template = cms.PSetTemplate(
        phase = cms.required.uint32,
        conversionFactor = cms.required.double,
        conversionFactorL1 = cms.required.double,
        offset = cms.required.double,
        offsetL1 = cms.required.double
      )
    ),
    verbose = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
