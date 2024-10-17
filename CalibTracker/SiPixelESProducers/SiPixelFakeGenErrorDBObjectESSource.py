import FWCore.ParameterSet.Config as cms

def SiPixelFakeGenErrorDBObjectESSource(*args, **kwargs):
  mod = cms.ESSource('SiPixelFakeGenErrorDBObjectESSource',
    siPixelGenErrorCalibrations = cms.vstring(
      'CalibTracker/SiPixelESProducers/data/SiPixelTemplateDBObject_0T_phase1_BoR3_v1/generror_summary_zp0310.out',
      'CalibTracker/SiPixelESProducers/data/SiPixelTemplateDBObject_0T_phase1_BoR3_v1/generror_summary_zp0311.out',
      'CalibTracker/SiPixelESProducers/data/SiPixelTemplateDBObject_0T_phase1_BoR3_v1/generror_summary_zp0312.out',
      'CalibTracker/SiPixelESProducers/data/SiPixelTemplateDBObject_0T_phase1_BoR3_v1/generror_summary_zp0313.out',
      'CalibTracker/SiPixelESProducers/data/SiPixelTemplateDBObject_0T_phase1_BoR3_v1/generror_summary_zp0314.out',
      'CalibTracker/SiPixelESProducers/data/SiPixelTemplateDBObject_0T_phase1_BoR3_v1/generror_summary_zp0315.out'
    ),
    Version = cms.double(1),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
