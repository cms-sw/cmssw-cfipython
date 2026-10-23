import FWCore.ParameterSet.Config as cms

def RunInfoTestESProducer(*args, **kwargs):
  mod = cms.ESProducer('RunInfoTestESProducer',
    runInfos = cms.VPSet(
      template = cms.PSetTemplate(
        run = cms.required.int32,
        start_time = cms.int64(0),
        start_time_str = cms.string(''),
        stop_time = cms.int64(0),
        stop_time_str = cms.string(''),
        fed_in = cms.vint32(),
        start_current = cms.double(0),
        stop_current = cms.double(0),
        avg_current = cms.double(0),
        min_current = cms.double(0),
        max_current = cms.double(0),
        run_intervall_micros = cms.double(0),
        current = cms.vdouble(),
        times_of_currents = cms.vdouble()
      )
    ),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
